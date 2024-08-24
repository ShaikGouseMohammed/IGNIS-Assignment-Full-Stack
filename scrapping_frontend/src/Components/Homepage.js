import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Container, Row, Col, Card, Form } from 'react-bootstrap';

const HomePage = () => {
    const [products, setProducts] = useState([]);
    const [searchTerm, setSearchTerm] = useState(''); // State for filtering

    useEffect(() => {
        axios.get('http://localhost:8000/api/products/')
            .then(response => setProducts(response.data))
            .catch(error => console.error('Error fetching products:', error));
    }, []);

    const formatProductName = (name) => {
        return name
    };

    // Filtered products based on search term
    const filteredProducts = products.filter(product =>
        product.title.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <Container>
            <h1 className="text-center my-4">Products</h1>
            <Form className="mb-4">
                <Form.Group controlId="search">
                    <Form.Control
                        type="text"
                        placeholder="Search products..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                </Form.Group>
            </Form>
            <Row>
                {filteredProducts.map((product, index) => (
                    <Col md={4} key={index} className="mb-4">
                        <Card className="product-card">
                            <Card.Body>
                                <Card.Title>
                                    <Link to={`/product/${formatProductName(product.title)}`}>
                                        {product.title}
                                    </Link>
                                </Card.Title>
                                <Card.Text><strong>Price:</strong> ${product.price}</Card.Text>
                               
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default HomePage;
