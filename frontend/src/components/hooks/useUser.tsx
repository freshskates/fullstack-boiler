import { useLocalStorage } from "usehooks-ts";
import { jwtDecode } from "jwt-decode";

type UserPayload = {
  sub: string;
  email: string;
  exp: number;
};

export function useUser() {
  const [token, setToken] = useLocalStorage<string | null>("authToken", null);

  let user: UserPayload | null = null;
  let isExpired = false;

  if (token) {
    try {
      user = jwtDecode<UserPayload>(token);
      isExpired = user.exp * 1000 < Date.now();
    } catch (error) {
      console.error("Invalid token:", error);
      setToken(null);
    }
  }

  const logout = () => setToken(null);

  return {
    user: isExpired ? null : user,
    isLoggedIn: !!user && !isExpired,
    getToken: () => token,
    setToken,
    logout,
  };
}
