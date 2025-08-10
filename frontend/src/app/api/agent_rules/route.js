import { NextResponse } from "next/server";
import path from "path";
import fs from "fs";

const RULES_PATH = path.join(__dirname, "../../../../.coai/rules/agent_rules.txt");

export async function GET() {
  let rules = "";
  if (fs.existsSync(RULES_PATH)) {
    rules = fs.readFileSync(RULES_PATH, "utf-8");
  }
  return NextResponse.json({ rules });
}

export async function POST(request) {
  const { rules } = await request.json();
  try {
    fs.writeFileSync(RULES_PATH, rules, "utf-8");
    return NextResponse.json({ success: true });
  } catch (e) {
    return NextResponse.json({ success: false, error: e.message }, { status: 500 });
  }
}
