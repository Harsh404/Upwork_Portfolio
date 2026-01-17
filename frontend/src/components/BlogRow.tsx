interface Blog {
  id: string;
  title: string;
  tags: string[];
  is_published: boolean;
  created_at: string;
}

interface Props {
  blog: Blog;
  onTogglePublish: (id: string, value: boolean) => void;
}

const BlogRow = ({ blog, onTogglePublish }: Props) => {
  return (
    <div className="flex justify-between items-center bg-white p-4 shadow rounded mb-2">
      <div>
        <h4 className="font-semibold">{blog.title}</h4>
        <p className="text-sm text-gray-500">
          {blog.tags.join(", ")}
        </p>
      </div>

      <button
        onClick={() => onTogglePublish(blog.id, !blog.is_published)}
        className={`px-3 py-1 rounded text-sm ${
          blog.is_published
            ? "bg-green-100 text-green-700"
            : "bg-gray-200 text-gray-700"
        }`}
      >
        {blog.is_published ? "Published" : "Draft"}
      </button>
    </div>
  );
};

export default BlogRow;
