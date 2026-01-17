const AdminDashboard = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-800 mb-8 text-center">Admin Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <h3 className="text-lg font-semibold mb-2">Manage Projects</h3>
          <p className="text-gray-600">Add, edit, delete projects</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <h3 className="text-lg font-semibold mb-2">Manage Blogs</h3>
          <p className="text-gray-600">Create and publish blogs</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <h3 className="text-lg font-semibold mb-2">View Contacts</h3>
          <p className="text-gray-600">Check contact messages</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <h3 className="text-lg font-semibold mb-2">Manage Media</h3>
          <p className="text-gray-600">Upload and organize files</p>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;