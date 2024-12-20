export const Footer = () => {
    return (
        <footer className="bg-gray-800 text-white py-8">
            <div className="container mx-auto px-4">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div>
                        <h3 className="text-lg font-bold mb-4">About Us</h3>
                        <p>Your company description here.</p>
                    </div>
                    <div>
                        <h3 className="text-lg font-bold mb-4">Quick Links</h3>
                        <ul>
                            <li><a href="/" className="hover:text-blue-300">Home</a></li>
                            <li><a href="/about" className="hover:text-blue-300">About</a></li>
                            <li><a href="/contact" className="hover:text-blue-300">Contact</a></li>
                        </ul>
                    </div>
                    <div>
                        <h3 className="text-lg font-bold mb-4">Contact</h3>
                        <p>Email: info@example.com</p>
                        <p>Phone: (123) 456-7890</p>
                    </div>
                </div>
            </div>
        </footer>
    );
};