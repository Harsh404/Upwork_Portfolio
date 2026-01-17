import AdminCard from "../components/AdminCard";

const AdminDashboard = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-800 mb-8 text-center">
        Admin Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <AdminCard
          title="Manage Projects"
          description="Add, edit, delete projects"
          route="/admin/projects"
        />
        <AdminCard
          title="Manage Blogs"
          description="Create and publish blogs"
          route="/admin/blogs"
        />
        <AdminCard
          title="View Contacts"
          description="Check contact messages"
          route="/admin/contacts"
        />
        <AdminCard
          title="Manage Media"
          description="Upload and organize files"
          route="/admin/media"
        />
      </div>
    </div>
  );
};

export default AdminDashboard;
