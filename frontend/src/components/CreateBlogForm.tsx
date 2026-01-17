import { useState } from "react";
import { createBlog } from "../api/admin.api";

interface Props {
  onSuccess: () => void;
}

const CreateBlogForm = ({ onSuccess }: Props) => {
  const [form, setForm] = useState({
    title: "",
    content: "",
    tags: "",
    is_published: true,
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value, type, checked } = e.target as any;
    setForm({ ...form, [name]: type === "checkbox" ? checked : value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      await createBlog({
        title: form.title,
        content: form.content,
        tags: form.tags.split(",").map(t => t.trim()),
        is_published: form.is_published,
      });

      setForm({
        title: "",
        content: "",
        tags: "",
        is_published: true,
      });

      onSuccess();
    } catch {
      alert("Failed to create blog");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-6 rounded-lg shadow mb-6"
    >
      <h3 className="text-xl font-semibold mb-4">Create Blog</h3>

      <input
        name="title"
        placeholder="Blog title"
        value={form.title}
        onChange={handleChange}
        required
        className="w-full mb-3 p-2 border rounded"
      />

      <textarea
        name="content"
        placeholder="Blog content"
        value={form.content}
        onChange={handleChange}
        rows={6}
        required
        className="w-full mb-3 p-2 border rounded"
      />

      <input
        name="tags"
        placeholder="Tags (comma separated)"
        value={form.tags}
        onChange={handleChange}
        className="w-full mb-3 p-2 border rounded"
      />

      <label className="flex items-center gap-2 mb-4">
        <input
          type="checkbox"
          name="is_published"
          checked={form.is_published}
          onChange={handleChange}
        />
        Publish immediately
      </label>

      <button
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        {loading ? "Creating..." : "Create Blog"}
      </button>
    </form>
  );
};

export default CreateBlogForm;
