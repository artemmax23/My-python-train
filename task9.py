def paginate (data: list, page: int, limit: int = 10) -> dict   
    total_items = len(data)
    total_pages = (total_items + limit - 1) // limit
    
    if page < 1:
        page = 1
    elif page > total_pages:
        page = total_pages
    
    start = (page - 1) * limit
    end = min(start + limit, total_items)
    returned_data = data[start:end]
        
    return {
        'data': returned_data, 
        'total_pages': total_pages, 
        'total_items': total_items, 
        'current_page': page, 
        'next_page': None if page >= total_pages else page + 1, 
        'prev_page': None if page < 2 else page - 1
    }
        
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(paginate(data, page=-20, limit=5))