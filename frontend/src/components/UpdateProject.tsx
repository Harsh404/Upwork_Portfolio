import { updateProject } from "../api/admin.api";
import { useState } from "react";

interface Props {
  project: any;
  onSuccess: () => void;
  onCancel?: () => void;
}

const UpdateProjectForm = ({ project, onSuccess, onCancel }: Props) => {
  const [form, setForm] = useState({
    title: project.title,
    description: project.description,
    tech_stack: project.tech_stack.join(", "),
    live_url: project.live_url || "",
    repo_url: project.repo_url || "",
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
      await updateProject(project.id, {
        title: form.title,
        description: form.description,
        tech_stack: form.tech_stack.split(",").map((t: string) => t.trim()),
        live_url: form.live_url || undefined,
        repo_url: form.repo_url || undefined,
      });

      onSuccess();
    } catch (err) {
      alert("Failed to update project");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow mb-6">
      <h3 className="text-xl font-semibold mb-4">Update Project</h3>

      <input
        name="title"
        placeholder="Title"
        value={form.title}
        onChange={handleChange}
        className="w-full mb-4 p-2 border border-gray-300 rounded"
        required
      />

      <textarea
        name="description"
        placeholder="Description"
        value={form.description}
        onChange={handleChange}
        className="w-full mb-4 p-2 border border-gray-300 rounded"
        required
      />

      <input
        name="tech_stack"
        placeholder="Tech Stack (comma separated)"
        value={form.tech_stack}
        onChange={handleChange}
        className="w-full mb-4 p-2 border border-gray-300 rounded"
        required
      />

      <input
        name="live_url"
        placeholder="Live URL"
        value={form.live_url}
        onChange={handleChange}
        className="w-full mb-4 p-2 border border-gray-300 rounded"
      />

      <input
        name="repo_url"
        placeholder="Repository URL"
        value={form.repo_url}
        onChange={handleChange}
        className="w-full mb-4 p-2 border border-gray-300 rounded"
      />

      <div className="flex gap-2">
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors duration-200"
          disabled={loading}
        >
          {loading ? "Updating..." : "Update Project"}
        </button>

        {onCancel && (
          <button
            type="button"
            onClick={onCancel}
            className="bg-gray-300 text-gray-800 px-4 py-2 rounded hover:bg-gray-400 transition-colors duration-200"
          >
            Cancel
          </button>
        )}
      </div>
    </form>
  );
};

export default UpdateProjectForm;
