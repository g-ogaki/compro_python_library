import { promises as fs } from "fs";
import path from "path";

export default async function Page() {
  const libraryPath = path.join(process.cwd(), "library");
  const items = await fs.readdir(libraryPath);

  return (
    <div className="max-w-3xl mx-auto py-10 px-4">
      <div className="bg-white shadow ring-1 ring-black ring-opacity-5 rounded-lg overflow-hidden">
        <div className="px-6 py-5 border-b border-gray-200 bg-gray-50">
          <h2 className="font-semibold text-gray-800">Algorithms / Data Structures</h2>
        </div>
        <ul className="divide-y divide-gray-200">
          {items.map((item) => (
            <li key={item}>
              <a
                href={`${item}/document`}
                className="flex justify-between items-center px-6 py-4 hover:bg-gray-50 transition-colors duration-150 group"
              >
                <span className="text-sm font-medium text-gray-700 group-hover:text-blue-600">
                  {item.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase())}
                </span>
                <span className="text-xs font-semibold text-blue-600 bg-blue-50 px-2 py-1 rounded-full opacity-0 group-hover:opacity-100 transition-opacity">
                  Open
                </span>
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}