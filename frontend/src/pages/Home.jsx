// src/pages/Home.jsx
import ChatWidget from '../components/chat/ChatWidget';
import ProductGrid from '../components/product/ProductGrid';

const Home = () => {
  const sampleProducts = [
    {
      id: 1,
      name: "Product 1",
      description: "Sample description",
      price: 99.99,
      image: "product-image-url",
      features: ["Feature 1", "Feature 2"]
    },
    // ... more products
  ];

  return (
    <div className="container mx-auto p-4">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <ProductGrid products={sampleProducts} />
        </div>
        <div>
            <ChatWidget />
        </div>
      </div>
    </div>
  );
};

export default Home;