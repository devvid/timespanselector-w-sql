export type Author = {
  id: number;
  name: string;
  email: string;
}

export type ViewHistory = {
  id: number,
  ipAddress: string,
  created: string
}
  
export type Post = {
  id: number;
  title: string;
  body: string;
  author: Author
  history: ViewHistory[]
}

export type PostHistory = {
  id: string,
  ipAddress: string,
  created: Date
}