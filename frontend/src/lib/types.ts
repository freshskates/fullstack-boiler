interface Post {
  id: string;
  title: string;
  content: string;
  createdAt: string;
}

interface User {
  id: string;
  email: string;
  name: string;
  createdAt: string;
  posts?: Post[];
}
