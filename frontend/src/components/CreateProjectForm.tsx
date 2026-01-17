import { useState } from "react";
import { createProject } from "../api/admin.api";

interface Props {
  onSuccess: () => void;
}

const CreateProjectForm = ({ onSuccess }: Props) => {
  const [form, setForm] = useState({
    title: "",
    description: "",
    tech_stack: "",
    live_url: "",
    repo_url: "",
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      await createProject({
        title: form.title,
        description: form.description,
        tech_stack: form.tech_stack.split(",").map(t => t.trim()),
        live_url: form.live_url || undefined,
        repo_url: form.repo_url || undefined,
      });

      setForm({
        title: "",
        description: "",
        tech_stack: "",
        live_url: "",
        repo_url: "",
      });

      onSuccess();
    } catch (err) {
      alert("Failed to create project");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow mb-6">
      <h3 className="text-xl font-semibold mb-4">Create Project</h3>

      <input
        name="title"
        placeholder="Title"
        value={form.title}
        onChange={handleChange}
        required
        className="w-full mb-3 p-2 border rounded"
      />

      <textarea
        name="description"
        placeholder="Description"
        value={form.description}
        onChange={handleChange}
        required
        className="w-full mb-3 p-2 border rounded"
      />

      <input
        name="tech_stack"
        placeholder="Tech stack (comma separated)"
        value={form.tech_stack}
        onChange={handleChange}
        required
        className="w-full mb-3 p-2 border rounded"
      />

      <input
        name="live_url"
        placeholder="Live URL (optional)"
        value={form.live_url}
        onChange={handleChange}
        className="w-full mb-3 p-2 border rounded"
      />

      <input
        name="repo_url"
        placeholder="Repo URL (optional)"
        value={form.repo_url}
        onChange={handleChange}
        className="w-full mb-3 p-2 border rounded"
      />

      <button
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        {loading ? "Creating..." : "Create Project"}
      </button>
    </form>
  );
};

export default CreateProjectForm;
