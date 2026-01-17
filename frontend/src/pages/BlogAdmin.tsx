import { useEffect, useState } from "react";
import { getBlogs, togglePublish } from "../api/admin.api";
import CreateBlogForm from "../components/CreateBlogForm";
import BlogRow from "../components/BlogRow";

const BlogsAdmin = () => {
  const [blogs, setBlogs] = useState<any[]>([]);

  const loadBlogs = async () => {
    const res = await getBlogs();
    setBlogs(res.data);
  };

  useEffect(() => {
    loadBlogs();
  }, []);

  const handleTogglePublish = async (id: string, value: boolean) => {
    await togglePublish(id, value);
    loadBlogs();
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Manage Blogs</h2>

      <CreateBlogForm onSuccess={loadBlogs} />

      {blogs.map(blog => (
        <BlogRow
          key={blog.id}
          blog={blog}
          onTogglePublish={handleTogglePublish}
        />
      ))}
    </div>
  );
};

export default BlogsAdmin;
