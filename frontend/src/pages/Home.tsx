const Home = () => {
  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold text-gray-800 mb-4">Welcome to My Portfolio</h1>
      <p className="text-lg text-gray-600 mb-8">
        Showcasing my projects, blogs, and services
      </p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-2">Projects</h2>
          <p className="text-gray-600">View my latest projects and work</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-2">Blogs</h2>
          <p className="text-gray-600">Read technical blogs and insights</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-2">Contact</h2>
          <p className="text-gray-600">Get in touch with me</p>
        </div>
      </div>
    </div>
  );
};

export default Home;