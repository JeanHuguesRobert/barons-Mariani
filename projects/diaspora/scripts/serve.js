import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { extname, join, normalize, sep } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));
const port = Number(process.env.PORT || 8765);
const types = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".md": "text/markdown; charset=utf-8",
  ".svg": "image/svg+xml",
  ".txt": "text/plain; charset=utf-8"
};

function safePath(urlPath) {
  const decoded = decodeURIComponent((urlPath || "/").split("?")[0]);
  const relative = (decoded === "/" ? "web/index.html" : decoded.replace(/^[/\\]+/, "")).replaceAll("/", sep);
  const rootNorm = normalize(root);
  const full = normalize(join(rootNorm, relative));
  const prefix = rootNorm.endsWith(sep) ? rootNorm : rootNorm + sep;
  if (full !== rootNorm && !full.startsWith(prefix)) return null;
  return full;
}

const server = createServer(async (request, response) => {
  const decoded = decodeURIComponent((request.url || "/").split("?")[0]);
  if (decoded === "/" || decoded === "/web" || decoded === "/web/") {
    response.writeHead(302, { location: "/web/index.html" });
    response.end();
    return;
  }
  const path = safePath(request.url || "/");
  if (!path) {
    response.writeHead(400);
    response.end("bad path");
    return;
  }
  try {
    const body = await readFile(path);
    response.writeHead(200, { "content-type": types[extname(path)] || "application/octet-stream" });
    response.end(body);
  } catch {
    response.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
    response.end("not found");
  }
});

server.listen(port, "127.0.0.1", () => {
  console.log(`DIASPORA static server http://127.0.0.1:${port}/`);
});
