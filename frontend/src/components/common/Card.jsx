export const Card = ({ children, className = '', ...props }) => {
    return (
        <div
            className={`rounded-lg shadow-md p-4 bg-white ${className}`}
            {...props}
        >
            {children}
        </div>
    );
};