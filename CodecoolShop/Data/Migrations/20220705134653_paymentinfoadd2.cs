using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Data.Migrations
{
    public partial class paymentinfoadd2 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<int>(
                name: "PaymentInfoId",
                table: "Orders",
                type: "int",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.CreateIndex(
                name: "IX_Orders_PaymentInfoId",
                table: "Orders",
                column: "PaymentInfoId");

            migrationBuilder.AddForeignKey(
                name: "FK_Orders_PaymentInfos_PaymentInfoId",
                table: "Orders",
                column: "PaymentInfoId",
                principalTable: "PaymentInfos",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Orders_PaymentInfos_PaymentInfoId",
                table: "Orders");

            migrationBuilder.DropIndex(
                name: "IX_Orders_PaymentInfoId",
                table: "Orders");

            migrationBuilder.DropColumn(
                name: "PaymentInfoId",
                table: "Orders");
        }
    }
}
