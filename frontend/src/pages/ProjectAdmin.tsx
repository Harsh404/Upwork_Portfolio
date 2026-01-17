import { useEffect, useState } from "react";
import { getProjects } from "../api/admin.api";
import CreateProjectForm from "../components/CreateProjectForm";
import Button from "../components/Button";
import UpdateProjectForm from "../components/UpdateProject";

const ProjectsAdmin = () => {
  const [projects, setProjects] = useState<any[]>([]);
  const [editingProject, setEditingProject] = useState<any>(null);

  const loadProjects = async () => {
    const res = await getProjects();
    setProjects(res.data);
  };

  useEffect(() => {
    loadProjects();
  }, []);

  const handleEdit = (project: any) => {
    setEditingProject(project);
  };

  const handleUpdateSuccess = () => {
    setEditingProject(null);
    loadProjects();
  };

  return (
    <div className="relative">
      <h2 className="text-2xl font-bold mb-4">Manage Projects</h2>

      <CreateProjectForm onSuccess={loadProjects} />

      {/* Projects List */}
      {projects.map((p) => (
        <div
          key={p.id}
          className="bg-white p-4 rounded shadow mb-2 flex items-start justify-between"
        >
          <div>
            <h4 className="font-semibold">{p.title}</h4>
            <p className="text-sm text-gray-600">{p.description}</p>
          </div>

          <div className="flex gap-2">
            <Button variant="secondary" onClick={() => handleEdit(p)}>
              Edit
            </Button>

            <Button variant="primary" onClick={() => {}}>
              Delete
            </Button>
          </div>
        </div>
      ))}

      {/* Modal for UpdateProjectForm */}
      {editingProject && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
            <UpdateProjectForm
              project={editingProject}
              onSuccess={handleUpdateSuccess}
              onCancel={() => setEditingProject(null)}
            />
          </div>
        </div>
      )}
    </div>
  );
};

export default ProjectsAdmin;
