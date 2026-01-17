import jwtDecode from "jwt-decode";

export interface JwtPayload {
  user_id: string;
  username: string;
  role: string;
  exp: number;
}

export const decodeToken = (token: string): JwtPayload =>
  jwtDecode<JwtPayload>(token);

export const isTokenExpired = (token: string): boolean =>
  decodeToken(token).exp * 1000 < Date.now();
