import { useState, useEffect } from 'react';
import axios from 'axios';

interface Blog {
  id: string;
  title: string;
  content: string;
  tags: string[];
  author: string;
  created_at: string;
  updated_at: string;
  is_published: boolean;
}

const Blogs = () => {
  const [blogs, setBlogs] = useState<Blog[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBlogs = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/api/v1/blogs`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setBlogs(response.data);
      } catch (error) {
        console.error('Error fetching blogs:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchBlogs();
  }, []);

  if (loading) {
    return <div className="text-center">Loading blogs...</div>;
  }

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-800 mb-8 text-center">Technical Blogs</h1>
      <div className="space-y-6">
        {blogs.map((blog) => (
          <div key={blog.id} className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold mb-2">{blog.title}</h2>
            <div className="mb-4">
              {blog.tags.map((tag) => (
                <span key={tag} className="bg-green-100 text-green-800 px-2 py-1 rounded text-sm mr-2">
                  {tag}
                </span>
              ))}
            </div>
            <p className="text-gray-700 mb-4">{blog.content}</p>
            <div className="text-sm text-gray-500">
              <p>By {blog.author}</p>
              <p>Published: {new Date(blog.created_at).toLocaleDateString()}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Blogs;