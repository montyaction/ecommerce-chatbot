import { Outlet } from 'react-router-dom';
import Navbar from './Navbar';
import Footer from './Footer';

const MainLayout = () => {
  return (
    <div className="flex flex-col min-h-screen bg-gray-100"> {/* Background here */}
      <Navbar />
      <main className="flex-grow p-4"> {/* Add padding to main content */}
        <Outlet /> {/* This is where the child routes will render */}
      </main>
      <Footer />
    </div>
  );
};

export default MainLayout;