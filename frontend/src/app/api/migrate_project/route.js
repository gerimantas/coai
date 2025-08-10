import { NextResponse } from "next/server";
import path from "path";
import fs from "fs";

export async function POST(request) {
  const body = await request.json();
  const { src, name } = body;
  const destRoot = "C:\\ai_projects";
  if (!src || !name) {
    return NextResponse.json({ error: "Missing src or name" }, { status: 400 });
  }
  const destDir = path.join(destRoot, name);
  if (!fs.existsSync(src)) {
    return NextResponse.json({ error: "Source directory not found" }, { status: 404 });
  }
  if (fs.existsSync(destDir)) {
    return NextResponse.json({ error: "Destination project already exists" }, { status: 409 });
  }
  try {
    fs.cpSync(src, destDir, { recursive: true });
    return NextResponse.json({ success: true, dest: destDir });
  } catch (e) {
    return NextResponse.json({ error: e.message }, { status: 500 });
  }
}
