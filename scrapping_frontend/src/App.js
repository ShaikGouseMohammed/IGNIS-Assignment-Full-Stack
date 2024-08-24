import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Components/Homepage';
import ProductDetailPage from './Components/ProductDetail';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/product/:name" element={<ProductDetailPage />} /> {/* Use `name` in the route */}
            </Routes>
        </Router>
    );
};

export default App;
