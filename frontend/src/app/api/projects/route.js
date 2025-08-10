import { NextResponse } from "next/server";
import path from "path";
import fs from "fs";

export async function GET() {
  // Projects root is now C:\ai_projects
  const projectsDir = "C:\\ai_projects";
  let projects = [];
  try {
    if (fs.existsSync(projectsDir)) {
      projects = fs.readdirSync(projectsDir).filter((d) => {
        return fs.statSync(path.join(projectsDir, d)).isDirectory();
      });
    }
  } catch (e) {
    return NextResponse.json({ projects: [], error: "Failed to read projects" }, { status: 500 });
  }
  return NextResponse.json({ projects });
}
