

# 📘 README – Docstring Style Detection  

Hum jab Python me function likhte hain to upar docstring dete hain (explain karne ke liye).  
SDK ka ek function hota hai jo check karta hai ke docstring ka **style** konsa hai:  
- Google  
- Numpy  
- Sphinx  

Aur fir us hisaab se **score assign** hota hai.  

---

## 🔎 Detection ka Process

1. Tum function ke upar docstring likhte ho (Google / Numpy / Sphinx format me).  
2. SDK ka `_detect_docstring_style` function docstring text ko line by line check karta hai.  
3. Jo pattern match karega usko **score** milega.  
4. Agar equal score ho gaya → **priority list** follow hogi:

Sphinx > Numpy > Google

Matlab tie ho to Sphinx jeet jaata hai.  

---

## ⚡ Example Code

### Google Style
```python
def add(a, b):
    """
    Args:
        a (int): First number
        b (int): Second number
    Returns:
        int: Sum of a and b
    """
    return a + b

✅ Ye Google style hai → isko Google score milega.


---

Numpy Style

def multiply(a, b):
    """
    Parameters
    ----------
    a : int
        First number
    b : int
        Second number
    
    Returns
    -------
    int
        Multiplication result
    """
    return a * b

✅ Ye Numpy style hai → Numpy score milega.


---

Sphinx Style

def divide(a, b):
    """
    :param a: First number
    :param b: Second number
    :return: Division result
    """
    return a / b

✅ Ye Sphinx style hai → Sphinx score milega.


---





📝## Summary

Tum jo style likhte ho wahi detect hota hai.

Jo match karega usko score milega, baaki 0.

Agar tie ho to Sphinx > Numpy > Google rule apply hota hai.



---

🔥 Ab tumhe clear hai ke score hum developer nahi dete, balki SDK ka function dete hai jo docstring ke format ko analyze karta hai.

--
