import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './store/AuthContext';
import MainLayout from './components/layout/MainLayout'; // Import the layout
import Home from './pages/Home';
import AuthPage from './pages/Auth';
import ForgotPasswordForm from './components/auth/ForgotPasswordForm';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route element={<MainLayout />}> {/* Use the layout as a parent route */}
            <Route path="/" element={<Home />} />
            <Route path="/auth" element={<AuthPage />} />
            <Route path="/forgot-password" element={<ForgotPasswordForm />} />
          </Route>
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;