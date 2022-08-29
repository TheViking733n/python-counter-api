import requests

"""
Simple class with no error checking like:
don't create a variable if it already exists, or
don't read value of a variable if it doesn't exists.
This is just a simple url and command wrapper
In case of error, all the method returns None

For docs refer: https://countapi.xyz/
"""

class CounterApi():
    endpoint = "https://api.countapi.xyz/"
    def __init__(self, variable, namespace="example_site.com"):
        self.variable = variable
        self.namespace = namespace
    
    def __str__(self):
        return self.variable + ": " + str(self.value())
        
    def value(self):
        """
        Returns the value of the variable using /get/ command
        """
        url = self.endpoint + "get/" + self.namespace + "/" + self.variable
        response = requests.get(url)

        if 'value' in response.json():
            return response.json()['value']
        else:
            return None
    
    def hit(self):
        """
        Increments the value of the variable by 1 using /hit/ command
        """
        url = self.endpoint + "hit/" + self.namespace + "/" + self.variable
        response = requests.get(url)

        if 'value' in response.json():
            return response.json()['value']
        else:
            return None

    def create(self, initial_value=0, allow_reset=True, increment_lowerbound=-1000000, increment_upperbound=1000000):
        """
        Creates a new variable of name self.variable
        initial_value: The initial value of the variable
        allow_reset: If True, variable value can be modified
        increment_lowerbound: Maximum value by which variable can be decreased
        increment_upperbound: Maximum value by which variable can be increased
        """
        data = {
            'key': self.variable,
            'namespace': self.namespace,
            'value': initial_value,
            'enable_reset': int(allow_reset),
            'update_lowerbound': increment_lowerbound,
            'update_upperbound': increment_upperbound
        }
        url = self.endpoint + "create"
        response = requests.get(url, params=data)
        if 'value' in response.json():
            return response.json()['value']
        else:
            return None
    
    def reset(self, new_value):
        """
        Resets the value of the variable to new_value
        Returns the old value of the variable
        """
        data = {
            'value': new_value
        }
        url = self.endpoint + "set/" + self.namespace + "/" + self.variable
        response = requests.get(url, params=data)
        if 'old_value' in response.json():
            return response.json()['old_value']
        else:
            return None

    def increment(self, delta):
        """
        Increments the value of the variable by delta
        Returns the updated of the variable
        """
        data = {
            'amount': delta
        }
        url = self.endpoint + "update/" + self.namespace + "/" + self.variable
        response = requests.get(url, params=data)
        if 'value' in response.json():
            return response.json()['value']
        else:
            return None
    
