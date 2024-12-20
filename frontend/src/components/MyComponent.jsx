import { useAuth } from '../store/AuthContext';

const MyComponent = () => {
    const { user, login, logout, loading, error } = useAuth();

    if (loading) {
        return <div>Loading...</div>
    }

    if (error) {
        return <div>Error: {error}</div>
    }

    return (
        <div>
            {user ? (
                <div>
                    <p>Welcome, {user.username}!</p>
                    <button onClick={logout}>Logout</button>
                </div>
            ) : (
                <button onClick={() => login({email: "test@test.com", password: "password"})}>Login</button>
            )}
        </div>
    );
};

export default MyComponent;