"use client";

import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { indentUnit } from "@codemirror/language";

export default function CodeEditor({ value, onChange }: { value: string; onChange: (value: string) => void }) {
  return (
    <CodeMirror
      value={value}
      height="auto"
      minHeight="300px"
      onChange={onChange}
      extensions={[python(), indentUnit.of("    ")]}
    />
  );
}
