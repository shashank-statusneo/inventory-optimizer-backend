"""empty message

Revision ID: b1096a5e7bee
Revises: 
Create Date: 2023-07-19 13:50:08.440336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1096a5e7bee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('destination_coordinates',
    sa.Column('destination_id', sa.String(length=50), nullable=False),
    sa.Column('destination_latitude', sa.String(length=50), nullable=False),
    sa.Column('destination_longitude', sa.String(length=50), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('distance_matrix',
    sa.Column('start_node', sa.String(length=50), nullable=False),
    sa.Column('end_node', sa.String(length=50), nullable=False),
    sa.Column('distance', sa.Integer(), nullable=False),
    sa.Column('time', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fleet_details',
    sa.Column('vehicle_type', sa.String(length=50), nullable=False),
    sa.Column('vehicle_count', sa.Integer(), nullable=False),
    sa.Column('fixed_cost', sa.Float(), nullable=False),
    sa.Column('variable_cost_per_km', sa.Float(), nullable=False),
    sa.Column('capacity_kg', sa.Float(), nullable=False),
    sa.Column('avg_speed_kmph', sa.Float(), nullable=False),
    sa.Column('characteristics', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('master_data',
    sa.Column('file_name', sa.String(length=100), nullable=False),
    sa.Column('file_type', sa.String(length=50), nullable=False),
    sa.Column('file_ext', sa.String(length=50), nullable=True),
    sa.Column('file_object', sa.BLOB(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_details',
    sa.Column('order_id', sa.String(length=50), nullable=False),
    sa.Column('destination', sa.String(length=50), nullable=False),
    sa.Column('order_weight', sa.Double(), nullable=False),
    sa.Column('order_volume', sa.Double(), nullable=False),
    sa.Column('delivery_slot_start_time', sa.DateTime(), nullable=False),
    sa.Column('delivery_slot_end_time', sa.DateTime(), nullable=False),
    sa.Column('special_vehicle_requirements', sa.String(length=50), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('source_coordinates',
    sa.Column('hub_id', sa.String(length=50), nullable=False),
    sa.Column('hub_latitude', sa.String(length=50), nullable=False),
    sa.Column('hub_longitude', sa.String(length=50), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle_availability',
    sa.Column('vehicle_id', sa.String(length=50), nullable=False),
    sa.Column('availability_start_time', sa.DateTime(), nullable=False),
    sa.Column('availability_end_time', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warehouse',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('demand_forecast',
    sa.Column('master_id', sa.Integer(), nullable=True),
    sa.Column('weekend', sa.DateTime(), nullable=False),
    sa.Column('month_no', sa.Integer(), nullable=False),
    sa.Column('month_week', sa.Integer(), nullable=False),
    sa.Column('article', sa.String(length=50), nullable=False),
    sa.Column('site', sa.String(length=50), nullable=False),
    sa.Column('predict', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['master_id'], ['master_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('input_benchmark_productivity',
    sa.Column('warehouse_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('productivity_experienced_employee', sa.Float(), nullable=False),
    sa.Column('productivity_new_employee', sa.Float(), nullable=False),
    sa.Column('soft_delete_flag', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['warehouse_id'], ['warehouse.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('warehouse_id', 'category_id')
    )
    op.create_table('input_demand',
    sa.Column('warehouse_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('demand', sa.Integer(), nullable=False),
    sa.Column('soft_delete_flag', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['warehouse_id'], ['warehouse.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('warehouse_id', 'category_id', 'date')
    )
    op.create_table('input_requirements',
    sa.Column('warehouse_id', sa.Integer(), nullable=True),
    sa.Column('num_current_employees', sa.Integer(), nullable=False),
    sa.Column('plan_from_date', sa.Date(), nullable=True),
    sa.Column('plan_to_date', sa.Date(), nullable=True),
    sa.Column('percentage_absent_expected', sa.Float(), nullable=False),
    sa.Column('day_working_hours', sa.Integer(), nullable=False),
    sa.Column('cost_per_employee_per_month', sa.Integer(), nullable=False),
    sa.Column('total_hiring_budget', sa.Integer(), nullable=False),
    sa.Column('soft_delete_flag', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['warehouse_id'], ['warehouse.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendor',
    sa.Column('master_id', sa.Integer(), nullable=True),
    sa.Column('vendor_id', sa.String(length=50), nullable=False),
    sa.Column('lead_time_avg', sa.Float(), nullable=False),
    sa.Column('lead_time_std_dev', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('order_cost', sa.Float(), nullable=False),
    sa.Column('stockout_cost', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['master_id'], ['master_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendor')
    op.drop_table('input_requirements')
    op.drop_table('input_demand')
    op.drop_table('input_benchmark_productivity')
    op.drop_table('demand_forecast')
    op.drop_table('warehouse')
    op.drop_table('vehicle_availability')
    op.drop_table('source_coordinates')
    op.drop_table('order_details')
    op.drop_table('master_data')
    op.drop_table('fleet_details')
    op.drop_table('distance_matrix')
    op.drop_table('destination_coordinates')
    op.drop_table('category')
    # ### end Alembic commands ###
