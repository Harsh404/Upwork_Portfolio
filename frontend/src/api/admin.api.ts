import api from "./api";


export interface CreateProjectPayload {
  title: string;
  description: string;
  tech_stack: string[];
  live_url?: string;
  repo_url?: string;
}

export const createProject = (data: CreateProjectPayload) =>
  api.post("/projects", data);

export const getProjects = () =>
  api.get("/projects");

export const updateProject = (id: string, data: Partial<CreateProjectPayload>) =>
  api.put(`/projects/${id}`, data);



export interface CreateBlogPayload {
  title: string;
  content: string;
  tags: string[];
  is_published: boolean;
}

export const getBlogs = () =>
  api.get("/api/v1/blogs/admin");

export const createBlog = (data: CreateBlogPayload) =>
  api.post("/api/v1/blogs", data);

export const togglePublish = (id: string, is_published: boolean) =>
  api.patch(`/api/v1/blogs/${id}`, { is_published });

