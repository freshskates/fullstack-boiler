import React from "react";
import { Avatar, AvatarFallback, AvatarImage } from "../ui/avatar";

interface AvatarProps {
  imageUrl?: string;
}

function UserAvatar({ imageUrl }: AvatarProps) {
  const imageUrl_ = imageUrl ? imageUrl : "https://github.com/shadcn.png";

  return (
    <Avatar className="h-10 w-10 rounded-full">
      <AvatarImage src={imageUrl_} alt="@shadcn" />
      <AvatarFallback>CN</AvatarFallback>
    </Avatar>
  );
}

export default UserAvatar;
