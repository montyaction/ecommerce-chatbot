// src/components/product/ProductDetail.jsx
const ProductDetail = ({ product }) => {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="aspect-w-1 aspect-h-1">
            <img
              src={product.image}
              alt={product.name}
              className="w-full h-full object-cover rounded-lg"
            />
          </div>
          
          <div className="space-y-4">
            <h1 className="text-3xl font-bold">{product.name}</h1>
            <p className="text-gray-600">{product.description}</p>
            
            <div className="text-2xl font-bold text-blue-600">
              ${product.price.toFixed(2)}
            </div>
            
            <div className="space-y-4">
              <div className="flex items-center space-x-2">
                <span className="text-gray-600">Quantity:</span>
                <select className="border rounded-lg p-2">
                  {[1, 2, 3, 4, 5].map((num) => (
                    <option key={num} value={num}>
                      {num}
                    </option>
                  ))}
                </select>
              </div>
              
              <button className="w-full py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">
                Add to Cart
              </button>
            </div>
            
            <div className="border-t pt-4 mt-4">
              <h3 className="font-semibold mb-2">Product Details</h3>
              <ul className="list-disc list-inside space-y-1 text-gray-600">
                {product.features?.map((feature, index) => (
                  <li key={index}>{feature}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    );
  };
  
  export default ProductDetail;