import React from 'react';
import { render, screen } from '@testing-library/react';
import Loader from '../ui/Loader';
import '@testing-library/jest-dom';

describe('Loader component', () => {
  it('renders loader', () => {
    render(<Loader />);
    expect(screen.getByTestId('loader')).toBeInTheDocument();
  });
});
