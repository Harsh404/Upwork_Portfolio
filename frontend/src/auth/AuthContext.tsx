import { createContext, useContext, useEffect, useState, ReactNode } from "react";
import api from "../api/api";
import { decodeToken, JwtPayload,isTokenExpired } from "./auth_utils";


interface AuthContextType {
  user: JwtPayload | null;
  login: (username: string, password: string) => Promise<void>;
  register: (username: string, email: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
  isAdmin: boolean;
  isAuthLoading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
};

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<JwtPayload | null>(null);
  const [isAuthLoading, setIsAuthLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (token && !isTokenExpired(token)) {
      setUser(decodeToken(token));
    } else {
      localStorage.clear();
      setUser(null);
    }

    setIsAuthLoading(false);
  }, []);

  const login = async (username: string, password: string) => {
    const response = await api.post(
      "/auth/login",
      new URLSearchParams({ username, password }),
      { headers: { "Content-Type": "application/x-www-form-urlencoded" } }
    );

    const { access_token, refresh_token } = response.data;

    localStorage.setItem("access_token", access_token);
    localStorage.setItem("refresh_token", refresh_token);

    setUser(decodeToken(access_token));
  };

  const register = async (username: string, email: string, password: string) => {
    await api.post("/auth/register", { username, email, password });
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        login,
        register,
        logout,
        isAuthenticated: !!user,
        isAdmin: user?.role === "admin",
        isAuthLoading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
