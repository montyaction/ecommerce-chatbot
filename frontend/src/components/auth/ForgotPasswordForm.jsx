import { useState } from 'react';
import { Mail } from 'lucide-react';

const ForgotPasswordForm = () => {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('');
        setError('');

        try {
            // Simulate API call - replace with your actual API endpoint
            await new Promise(resolve => setTimeout(resolve, 1000));

            // In a real app, you would send a password reset email here
            console.log('Password reset requested for:', email);
            setMessage('If an account with that email exists, a reset link has been sent.');
        } catch (err) {
            setError('An error occurred. Please try again later.');
            console.error(err)
        }
    };

    return (
        <div className="w-full max-w-md mx-auto p-6 bg-white rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold text-center mb-6">Forgot Password</h2>
            {message && <div className="p-3 bg-green-100 border border-green-400 text-green-700 rounded mb-4">{message}</div>}
            {error && <div className="p-3 bg-red-100 border border-red-400 text-red-700 rounded mb-4">{error}</div>}
            <form onSubmit={handleSubmit} className="space-y-4">
                <div className="relative">
            <Mail className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>
                <button
                    type="submit"
                    className="w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50">
                    Reset Password
                </button>
            </form>
        </div>
    );
};

export default ForgotPasswordForm;