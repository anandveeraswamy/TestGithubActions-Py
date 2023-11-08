from triangle import area_of_a_triangle
import pytest

# use nose2 -v to display the docstring in the test results
# use the pytest.ini file to set the color and verbose output
# nose2 does not have color options but does display the docstring along with the class and function names
# Forget about adding good coloring as shown by the use of nose and pinnochio - I have tried to get this using nose2 but does not work
# https://coverage.readthedocs.io/en/7.3.2/ see this link to see how to run the coverage tool

class TestAreaOfTriangle():    
    def test_float_values(self):
        """ Test areas when values are floats """        
        assert 14.43870626 == area_of_a_triangle(3.4556, 8.3567)        
        assert pytest.approx(14.43870626) == area_of_a_triangle(3.4556, 8.3567)        
        assert 6.555 == area_of_a_triangle(2.3, 5.7)

    def test_integer_values(self):
        """ Test areas when values are integers """        
        assert 5.0 == area_of_a_triangle(2,5)        
        assert 10.0 == area_of_a_triangle(4,6)

    def test_zero_base(self):
        """ Test areas when base is zero """        
        assert 0.0 == area_of_a_triangle(0, 5)

    def test_zero_height(self):
        """ Test areas when height is zero """        
        assert 0.0 == area_of_a_triangle(2, 0)

    def test_zero_values(self):
        """ Test areas when base and height are zero """        
        assert 0.0 == area_of_a_triangle(0, 0)

    def test_negative_base(self):
        """ Test that ValueError is raised when base is negative """        
        pytest.raises(ValueError, area_of_a_triangle, -2, 5)

    def test_negative_height(self):
        """ Test that ValueError is raised when height is negative """
        pytest.raises(ValueError, area_of_a_triangle, 2, -5)

    def test_negative_values(self):
        """ Test that ValueError is raised when both are negative """
        pytest.raises(ValueError, area_of_a_triangle, -2, -5)

    def test_with_boolean(self):
        """ Test that TypeError is raised with boolean types """
        pytest.raises(TypeError, area_of_a_triangle, True, 5)   # test booleans
        pytest.raises(TypeError, area_of_a_triangle, 2, True)

    def test_with_string(self):
        """ Test that TypeError is raised with string types """
        pytest.raises(TypeError, area_of_a_triangle, "base", 5) # test strings
        pytest.raises(TypeError, area_of_a_triangle, 2, "height")

    def test_with_nulls(self):
        """ Test that TypeError is raised with null types """
        pytest.raises(TypeError, area_of_a_triangle, None, 5) # test strings
        pytest.raises(TypeError, area_of_a_triangle, 2, None)
