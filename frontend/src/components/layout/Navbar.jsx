const Navbar = () => {
    return (
        <nav className="bg-white shadow-md py-4">
            <div className="container mx-auto px-4 flex justify-between items-center">
                <a href="/" className="text-xl font-bold">Logo</a>
                <div className="flex gap-4">
                    <a href="/" className="hover:text-blue-500">Home</a>
                    <a href="/about" className="hover:text-blue-500">About</a>
                    <a href="/contact" className="hover:text-blue-500">Contact</a>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;