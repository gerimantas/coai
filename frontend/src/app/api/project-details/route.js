import { NextResponse } from "next/server";
import path from "path";
import fs from "fs";

export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const name = searchParams.get("name");
  const root = "C:\\ai_projects";
  let config = null, rules = null, plan = null;
  if (name) {
    const configPath = path.join(root, name, "config.json");
    const rulesPath = path.join(root, name, "rules.txt");
    const planPath = path.join(root, name, "plan.md");
    if (fs.existsSync(configPath)) {
      config = JSON.parse(fs.readFileSync(configPath, "utf-8"));
    }
    if (fs.existsSync(rulesPath)) {
      rules = fs.readFileSync(rulesPath, "utf-8");
    }
    if (fs.existsSync(planPath)) {
      plan = fs.readFileSync(planPath, "utf-8");
    }
  }
  return NextResponse.json({ config, rules, plan });
}
