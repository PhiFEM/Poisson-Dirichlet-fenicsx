class ResultsSaver:

    def __init__(self, output_path) -> None: ...
        
    def add_new_value(self, key, value) -> None: ...
    
    def save_function(self, function, file_name) -> None: ...

    def save_mesh(self, mesh, file_name) -> None: ...
    
    def save_values(self, file_name) -> None: ...