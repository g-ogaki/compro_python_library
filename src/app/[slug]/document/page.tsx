import PythonRunner from "@/components/PythonRunner";
import path from "path";
import { promises as fs } from "fs";
import MarkdownRenderer from "@/components/MarkdownRenderer";

export async function generateStaticParams() {
  const libraryPath = path.join(process.cwd(), "library");
  const items = await fs.readdir(libraryPath);
  return items.map((item) => ({ slug: item }));
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const documentPath = path.join(process.cwd(), "library", slug, "README.md");
  const document = await fs.readFile(documentPath);
  const codePath = path.join(process.cwd(), "library", slug, "code.py");
  const code = await fs.readFile(codePath);

  return (
    <div className="flex flex-col w-full max-w-3xl px-4 py-10 mx-auto gap-4">
      <MarkdownRenderer>{document.toString()}</MarkdownRenderer>
      <PythonRunner defaultValue={code.toString()} />
    </div>
  );
}
