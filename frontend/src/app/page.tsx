"use client";
import { Button } from "@/components/ui/button";
import { formatDateTimeAgo } from "@/lib/utils";
import Image from "next/image";
import { useState } from "react";

export default function Home() {
  const [sortConfig, setSortConfig] = useState<{
    key: keyof (typeof posts)[number];
    direction: "asc" | "desc";
  } | null>(null);

  const [posts, setPosts] = useState([
    {
      content: "Another post",
      author: "user39",
      createdAt: "2025-03-07T01:20:00Z",
    },
    {
      content: "zllo, world!asd",
      author: "user39",
      createdAt: "2025-03-07T01:15:00Z",
    },
    {
      content: "Hello, world!",
      author: "user39",
      createdAt: "2025-03-07T01:12:00Z",
    },
  ]);

  const handleSort = (key: keyof (typeof posts)[number]) => {
    let direction: "asc" | "desc" = "asc";
    if (sortConfig?.key === key && sortConfig.direction === "asc") {
      direction = "desc";
    }
    setSortConfig({ key, direction });

    const sortedPosts = [...posts].sort((a, b) => {
      if (a[key] < b[key]) return direction === "asc" ? -1 : 1;
      if (a[key] > b[key]) return direction === "asc" ? 1 : -1;
      return 0;
    });

    setPosts(sortedPosts);
  };

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center justify-center ">
        <Button className="h-8">overview</Button>

        <div className="border-[0.5px] w-96 border-zinc-400 rounded-sm text-sm">
          <div className="px-4 pt-6 pb-2 text-zinc-800 flex justify-between text-xs">
            <div className="flex w-full justify-between bg-[#12201a] text-[#ffffff] rounded-sm p-2">
              <p>user39</p>
              <p>joined 2 days ago</p>
            </div>
          </div>

          <div className="flex flex-col space-y-2 p-2 text-xs">
            <table className="min-w-full border-collapse rounded-lg">
              <thead className=" ">
                <tr>
                  <th
                    className="px-4 py-2 text-left border-b border-zinc-300 select-none cursor-pointer hover:bg-zinc-100"
                    onClick={() => handleSort("content")}
                  >
                    Content{" "}
                    {sortConfig?.key === "content"
                      ? sortConfig.direction === "asc"
                        ? "^"
                        : "v"
                      : ""}
                  </th>
                  <th
                    className="px-4 py-2 text-right border-b border-zinc-300 select-none cursor-pointer hover:bg-zinc-100"
                    onClick={() => handleSort("createdAt")}
                  >
                    Date{" "}
                    {sortConfig?.key === "createdAt"
                      ? sortConfig.direction === "asc"
                        ? "^"
                        : "v"
                      : ""}
                  </th>
                </tr>
              </thead>
              <tbody>
                {posts.map((post, index) => (
                  <tr
                    key={index}
                    className="odd:bg-zinc-50 even:bg-white hover:bg-zinc-100 "
                  >
                    <td className="px-4 py-2 text-left border-zinc-300">
                      {post.content}
                    </td>
                    <td className="px-4 py-2 text-right  border-zinc-300">
                      {formatDateTimeAgo(post.createdAt)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}
