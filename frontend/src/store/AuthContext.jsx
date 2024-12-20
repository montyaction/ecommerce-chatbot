import { createContext, useState, useEffect } from 'react';
import authService from '../services/authServices';

// Auth Context
export const AuthContext = createContext(null);

// Auth Provider Component
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
      try {
        fetch('/api/me', {
          headers: {
            Authorization: `Bearer ${storedToken}`,
          },
        })
          .then((r) => r.json())
          .then((data) => {
            if (data.user) {
              setUser(data.user);
            }
          })
          .finally(() => setLoading(false));
      } catch (error) {
        console.error('Error fetching user data', error);
        setLoading(false);
      }
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (credentials) => {
    setLoading(true);
    setError(null);
    try {
      const response = await authService.login(credentials); // Use authService
      if (response.success) {
        setUser(response.user);
        localStorage.setItem('token', response.token); // Store the token
        return { success: true };
      } else {
        setError(response.error);
        return { success: false, error: response.error };
      }
    } catch (error) {
      setError(error.message);
      return { success: false, error: error.message };
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('user');
    localStorage.removeItem('token');
  };

  const register = async (credentials) => {
    setLoading(true);
    setError(null);
    try {
      const response = await authService.register(credentials); // Use authService
      if (response.success) {
        setUser(response.user);
        localStorage.setItem('token', response.token); // Store the token
        return { success: true };
      } else {
        setError(response.error);
        return { success: false, error: response.error };
      }
    } catch (error) {
      setError(error.message);
      return { success: false, error: error.message };
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, register, loading, error }}>
      {children}
    </AuthContext.Provider>
  );
};