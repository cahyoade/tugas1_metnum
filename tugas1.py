from sympy import *
x = Symbol('x')

f = x**3 - 5*x**2 + 7*x - 3
err = 0.000001

f_prime = f.diff(x)
f_double_prime = f_prime.diff(x)

f = lambdify(x, f)
f_prime = lambdify(x, f_prime)
f_double_prime = lambdify(x, f_double_prime)

def newton(guess, err, func, derivative):
    count = 1
    while abs(func(guess)) > err:
        fx = func(guess)
        dx = derivative(guess)

        print(f'#{count}. guess:{guess}, f(x):{fx}, f\'(x):{dx}, f(x)/f\'(x):{fx/dx}, next guess:{guess - fx/dx}')
        guess -= fx/dx
        count += 1

    return guess

def newton_modified(guess, err, func, derivative, derivative2):
    count = 1
    while abs(func(guess)) > err:
        fx = func(guess)
        dx = derivative(guess)
        dx2 = derivative2(guess)
        correction = (fx*dx) / ((dx**2) - (fx*dx2))

        print(f'#{count}. guess:{guess}, f(x):{fx}, u(x)/u\'(x):{correction}, next guess:{guess - correction}')
        guess -= correction
        count += 1

    return guess

def secant(guess, guess1, err, func):
    count = 1
    while abs(func(guess1)) > err:
        fx_r = func(guess)
        fx_r1 = func(guess1)
        correction = (fx_r1 * (guess1 - guess)) / (fx_r1 - fx_r)

        print(f'#{count}. xr-1:{guess}, xr:{guess1}, f(xr):{fx_r1}, koreksi:{correction}, xr+1:{guess1 - correction}')

        guess = guess1
        guess1 -= correction
        count += 1
    
    return guess

def secant_modified(guess, guess1, guess2, err, func):
    count = 1
    while abs(func(guess2)) > err:
        fx_r = func(guess)
        fx_r1 = func(guess1)
        fx_r2 = func(guess2)

        ux = (fx_r2 * (guess2 - guess1)) / (fx_r2 - fx_r1)
        ux1 = (fx_r1 * (guess1 - guess)) / (fx_r1 - fx_r)
        correction = (guess2 - guess1)/(1 - (ux1 / ux))

        print(f'#{count}. xr-2:{guess}, xr-1:{guess1}, xr:{guess2}, f(xr):{fx_r2}, koreksi:{correction}, xr+1:{guess2 - correction}')

        guess = guess1
        guess1 = guess2
        guess2 -= correction
        count += 1
    
    return guess

print('newton method :')
newton(1.9, err, f, f_prime)

print('\nmodified newton method :')
newton_modified(1.9, err, f, f_prime, f_double_prime)

print('\nsecant method :')
secant(2, 1.8, err, f)

print('\nmodified secant method :')
secant_modified(2, 1.9, 1.8, err, f)
