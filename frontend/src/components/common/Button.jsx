export const Button = ({ children, onClick, className = '', variant = 'secondary', ...props }) => {
    const baseStyles = 'px-4 py-2 rounded-md transition-colors';
    
    const variants = {
        primary: 'bg-blue-500 text-white hover:bg-blue-600',
        secondary: 'bg-gray-500 text-white hover:bg-gray-600',
        outline: 'border-2 border-blue-500 text-blue-500 hover:bg-blue-50'
    };

    return (
        <button
            onClick={onClick}
            className={`px-4 py-2 rounded-md bg-blue-500 text-white hover:bg-blue-600 ${className} ${baseStyles} ${variants[variant]}`}
            {...props}
        >
            {children}
        </button>
    );
};