import { useNavigate } from "react-router-dom";

interface AdminCardProps {
  title: string;
  description: string;
  route: string;
}

const AdminCard = ({ title, description, route }: AdminCardProps) => {
  const navigate = useNavigate();

  return (
    <div
      onClick={() => navigate(route)}
      className="bg-white p-6 rounded-lg shadow-md text-center cursor-pointer hover:shadow-lg transition"
    >
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  );
};

export default AdminCard;
