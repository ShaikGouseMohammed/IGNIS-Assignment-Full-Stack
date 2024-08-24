import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Container, Row, Col, Spinner, ListGroup, Card } from 'react-bootstrap';

const ProductDetailPage = () => {
    const { name } = useParams(); // Get the product name from the URL
    const [product, setProduct] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:8000/api/products/')
            .then(response => {
                // Convert the URL-friendly name back to the original name format
                const product = response.data.find(p => p.title === name);
                setProduct(product);
            })
            .catch(error => console.error('Error fetching product details:', error));
    }, [name]);

    if (!product) {
        return (
            <Container className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
                <Spinner animation="border" />
            </Container>
        ); // Show loading state while the product is being fetched
    }

    return (
        <Container>
            <Row>
                <Col md={{ span: 8, offset: 2 }}>
                    <Card className="product-detail-card">
                        <Card.Body>
                            <Card.Title className="mb-4">{product.title}</Card.Title>
                            <Card.Text><strong>Price:</strong> ${product.price}</Card.Text>
                            <Card.Text><strong>MRP:</strong> ${product.mrp}</Card.Text>
                            <Card.Text><strong>Fit:</strong> {product.fit}</Card.Text>
                            <Card.Text><strong>Fabric:</strong> {product.fabric}</Card.Text>
                            <Card.Text><strong>Neck:</strong> {product.neck}</Card.Text>
                            <Card.Text><strong>Sleeve:</strong> {product.sleeve}</Card.Text>
                            <Card.Text><strong>Length:</strong> {product.length}</Card.Text>
                            <Card.Text><strong>Pattern:</strong> {product.pattern}</Card.Text>
                            <Card.Text><strong>Description:</strong> {product.description}</Card.Text>
                            <Card.Text><strong>Available Colors and Sizes:</strong></Card.Text>
                            <ListGroup variant="flush">
                                {product.available_skus.map((sku, index) => (
                                    <ListGroup.Item key={index}>
                                        <strong>Color:</strong> {sku.color}, <strong>Sizes:</strong> {sku.size.join(', ')}
                                    </ListGroup.Item>
                                ))}
                            </ListGroup>
                            <Card.Text className="mt-4"><strong>Last 7 Day Sale:</strong> {product.last_7_day_sale}</Card.Text>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
};

export default ProductDetailPage;
