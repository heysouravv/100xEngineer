import { Application, Router } from "https://deno.land/x/oak@v12.6.0/mod.ts";

const app = new Application();
const router = new Router();

const memory: Record<string, string> = {};

router
  .post("/rem", async (ctx) => {
    const { name, value } = await ctx.request.body().value;

    if (value !== undefined) {
      memory[name] = value;
      ctx.response.body = `Saved '${name}' with value '${value}'`;
    } else {
      ctx.response.body = memory[name] || "Value not found";
    }
  })
  .post("/calc", async (ctx) => {
    const { expression } = await ctx.request.body().value;
    
    try {
      ctx.response.body = eval(expression).toString(); // Be cautious with eval
    } catch (e) {
      ctx.response.body = "Invalid expression";
    }
  });

app.use(router.routes());
app.use(router.allowedMethods());

console.log("Server is running on http://localhost:8000");
await app.listen({ port: 8000 });
