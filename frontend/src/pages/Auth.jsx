// Main Auth Component that wraps everything with AuthProvider
import { useState } from "react";
import LoginForm from "../components/auth/LoginForm";
import RegisterForm from "../components/auth/RegisterForm";
import { AuthProvider } from "../store/AuthContext";

const Auth = () => {
    const [isLogin, setIsLogin] = useState(true);

    return (
      <AuthProvider>
        <div className="min-h-screen bg-gray-100 flex flex-col justify-center py-12 px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold">Welcome</h1>
            <p className="mt-2 text-gray-600">
              {isLogin ? "Sign in to your account" : "Create a new account"}
            </p>
          </div>

          {isLogin ? <LoginForm /> : <RegisterForm />}

          <div className="text-center mt-4">
            <button
              onClick={() => setIsLogin(!isLogin)}
              className="text-blue-600 hover:text-blue-800"
            >
              {isLogin ? "Need an account? Sign up" : "Already have an account? Sign in"}
            </button>
          </div>
        </div>
      </AuthProvider>
    );
  };

  export default Auth;