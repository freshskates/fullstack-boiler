"use client";
import { useUser } from "@/components/hooks/useUser";
import { Button } from "@/components/ui/button";
import { formatDateTimeAgo } from "@/lib/utils";
import { useQuery } from "@tanstack/react-query";
import axios, { AxiosResponse } from "axios";
import Image from "next/image";
import Link from "next/link";
import { useState } from "react";

export default function Home() {
  const { user, getToken } = useUser();

  const [sortConfig, setSortConfig] = useState<{
    key: keyof (typeof posts)[number];
    direction: "asc" | "desc";
  } | null>(null);

  const [posts, setPosts] = useState<Post[]>([]);

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

  const { data, isLoading, isError } = useQuery<User>({
    queryKey: ["userData", user?.sub],
    queryFn: async (): Promise<User> => {
      if (!user?.sub) throw new Error("User not found");

      const token = getToken();
      if (!token) throw new Error("Token not found");

      const response: AxiosResponse<User> = await axios.get(
        `http://localhost:8000/users/me`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setPosts(response.data?.posts ?? []);

      return response.data;
    },
    enabled: !!user?.sub,
  });

  if (isLoading || isError) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen text-center">
        <div className="border border-zinc-300 rounded-md p-6 space-y-2 w-80 shadow-sm">
          <h2 className="text-lg text-zinc-800">Loading...</h2>
        </div>
      </div>
    );
  }

  if (!user || !data) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen text-center">
        <div className="border border-zinc-300 rounded-md p-6 space-y-2 w-80 shadow-sm">
          <h2 className="text-lg text-zinc-800">Not Logged In</h2>
          <p className="text-sm text-zinc-600 ">
            You need to sign in to access.
          </p>
          <Button className="h-8 mt-2">
            <Link href="/login">Login</Link>
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center justify-center ">
        <Button className="h-8">overview</Button>

        <div className="border-[0.5px] w-96 border-zinc-400 rounded-sm text-sm">
          <div className="px-4 pt-6 pb-2 text-zinc-800 flex justify-between text-xs">
            <div className="flex w-full justify-between bg-[#12201a] text-[#ffffff] rounded-sm p-2">
              <p>{user?.email}</p>
              <p>{formatDateTimeAgo(data.createdAt)}</p>
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
                {posts.length === 0 && (
                  <tr>
                    <td colSpan={2} className="px-4 py-2 text-center">
                      No posts found
                    </td>
                  </tr>
                )}

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
